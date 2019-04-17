FROM ubuntu:16.04
LABEL maintainer="David Manouchehri"

RUN apt-get update && apt-get dist-upgrade -y && \
    apt-get install -y git cmake build-essential ca-certificates curl wget  \
    software-properties-common unzip libboost-dev python-dev python-pip && apt-get clean

RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \
    apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-6.0 main" && \
    apt-get update && apt-get install -y clang-6.0 && apt-get clean && \
    cd /usr/bin && ln -s clang-6.0 clang && ln -s clang++-6.0 clang++

# get and install the latest z3 relesae
RUN cd /tmp && \
    curl -o z3.tgz -L  https://github.com/Z3Prover/z3/archive/z3-4.5.0.tar.gz && \
    tar zxf z3.tgz && cd z3-z3-4.5.0 && \
    CC=clang CXX=clang++ python scripts/mk_make.py && cd build && make \
    && make install && cd /tmp && rm /tmp/z3.tgz && rm -rf /tmp/z3-z3-4.5.0

# Install capstone
RUN cd /tmp && \
    curl -o cap.tgz -L https://github.com/aquynh/capstone/archive/3.0.4.tar.gz && \
    tar xvf cap.tgz && cd capstone-3.0.4/ && ./make.sh install && cd /tmp && \
    rm /tmp/cap.tgz && rm -rf /tmp/capstone-3.0.4


# Install pintool
RUN cd /opt && curl -o pin.tgz -L http://software.intel.com/sites/landingpage/pintool/downloads/pin-2.14-71313-gcc.4.4.7-linux.tar.gz && \
    tar zxf pin.tgz && rm pin.tgz

# now install Triton
# uncomment below to pull form git
# RUN cd /opt/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ && git clone https://github.com/JonathanSalwan/Triton.git && \
#     cd Triton && mkdir build && cd build && cmake -G "Unix Makefiles" -DPINTOOL=on -DKERNEL4=on .. && \
#     make install && cd .. && python setup.py install
RUN cd /opt/pin-2.14-71313-gcc.4.4.7-linux/source/tools/ && \
    curl -o triton.zip -L https://github.com/JonathanSalwan/Triton/archive/2838b732d6398b33f590f4db5d045c26054486ae.zip && \
    unzip triton.zip && rm triton.zip && cd Triton-2838b732d6398b33f590f4db5d045c26054486ae/ && mkdir build && cd build && \
    cmake -G "Unix Makefiles" -DPINTOOL=on -DKERNEL4=on .. && make install && cd ..

# Install Tigress_protection dependencies
RUN pip install --upgrade pip==9.0.1
RUN pip install setuptools --upgrade
RUN pip install llvmlite
RUN pip install https://github.com/quarkslab/arybo/archive/master.zip
RUN pip install https://github.com/lief-project/packages/raw/lief-master-latest/pylief-0.9.0.dev.zip

ENTRYPOINT /bin/bash

