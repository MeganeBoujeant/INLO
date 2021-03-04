import os

SAMPLE = ["S" + str(nb) for nb in range(10)] # Define some file prefix
SAMPLE_EVEN = ["S" + str(x) for x in range(0, 10, 2)]
SAMPLE_DICT = dict()

workdir: os.getcwd() # set a working dir

rule final:
    input: "step_4/all.txt",
           "step_5/all_even.txt",
           expand("step_6/{smp}.txt", smp = SAMPLE_DICT.keys())

rule step_1:
    output: "step_1/{smp}.txt"
    shell: """
    echo "{wildcards.smp} step_1"  > {output}
    """

rule step_2:
    input: "step_1/{smp}.txt"
    output: "step_2/{smp}.txt"
    shell: """
    cp {input} {output}
    echo "{wildcards.smp} step_2"  >> {output}
    """

rule step_3:
    input: "step_2/{smp}.txt"
    output: "step_3/{smp}.txt"
    shell: """
    cp {input} {output}
    echo "{wildcards.smp} step_3" >> {output}
    """

rule step_4:
    input: expand("step_3/{smp}.txt", smp=SAMPLE)
    output: "step_4/all.txt"
    shell: """
    cat {input}  >> {output}
    """

rule step_5:
    input: expand("step_3/{smp}.txt", smp=SAMPLE_EVEN)
    output: "step_5/all_even.txt"
    shell: """
    cat {input}  >> {output}
    """

def get_odd(wildcards):
    smp_odd = SAMPLE_DICT[wildcards.smp]
    path = os.path.join("step_3", smp_odd + ".txt")
    return path

rule step_6:
    input: a = "step_3/{smp}.txt", b=get_odd
    output: "step_6/{smp}.txt"
    shell: """
    cat {input.a} {input.b}  >> {output}
    """
