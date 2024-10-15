import streamlit as st
import pandas as pd
import numpy as np
import requests
import time


def get_statics():
    r = requests.get("http://localhost:8000/serve/static/")
    print(r)
    return r.json()


def get_machine_states():
    r = requests.get("http://localhost:8000/serve/machine/")
    return r.json()


def get_processes():
    r = requests.get("http://localhost:8000/serve/process/")
    return r.json()


statics = get_statics()

# get states and processes. Group by machine_id states and processes by machine_id and pid
states = get_machine_states()
processes = get_processes()

mach_cpu = {}
for state in states:
    if state["machine_id"] not in mach_cpu:
        mach_cpu[state["machine_id"]] = []
    mach_cpu[state["machine_id"]].append(state['cpu_percent'])

prs_cpu = {}
for process in processes:
    if process["machine_id"] not in prs_cpu:
        prs_cpu[process["machine_id"]] = {}
    if process['pid'] not in prs_cpu[process["machine_id"]]:
        prs_cpu[process["machine_id"]][process['pid']] = []
    prs_cpu[process["machine_id"]][process['pid']].append(
        process['cpu_percent'])

# display the data by machine_id

st.title("Machine Stats")
# option to select machine_id to display
machine_id = st.selectbox("Select Machine", list(mach_cpu.keys()))
st.write(f"Machine ID: {machine_id}")
st.write("Machine CPU Usage")
st.line_chart(mach_cpu[machine_id])
st.write("Process CPU Usage")
# display the processes cpu usage
st.write(prs_cpu[machine_id])
# display the data by pid
st.title("Process Stats")
# option to select pid to display
pid = st.selectbox("Select Process", list(prs_cpu[machine_id].keys()))
st.write(f"Process ID: {pid}")
st.write("Process CPU Usage")
st.line_chart(prs_cpu[machine_id][pid])


gpu_percent = {}
for state in states:
    if state["machine_id"] not in gpu_percent:
        gpu_percent[state["machine_id"]] = []
    gpu_percent[state["machine_id"]].append(state['gpu_memory_percent'])

prs_gpu_percent = {}
for process in processes:
    if process["machine_id"] not in prs_gpu_percent:
        prs_gpu_percent[process["machine_id"]] = {}
    if process['pid'] not in prs_gpu_percent[process["machine_id"]]:
        prs_gpu_percent[process["machine_id"]][process['pid']] = []
    prs_gpu_percent[process["machine_id"]][process['pid']].append(
        process['gpu_memory_percent'])

st.title("Machine GPU Stats")
# option to select machine_id to display
machine_id = st.selectbox("Select Machine gPU", list(gpu_percent.keys()))
st.write(f"Machine ID: {machine_id}")
st.write("Machine GPU Usage")
st.line_chart(gpu_percent[machine_id])
st.write("Process GPU Usage")
# display the processes cpu usage
# st.write(prs_gpu_percent[machine_id])
# display the data by pid
st.title("Process GPU Stats")
# option to select pid to display
pid = st.selectbox("Select Process 222", list(
    prs_gpu_percent[machine_id].keys()))
st.write(f"Process ID: {pid}")
st.write("Process GPU Usage")
st.line_chart(prs_gpu_percent[machine_id][pid])


# update realtime
# while True:
#     states = get_machine_states()
#     processes = get_processes()

#     mach_cpu = {}
#     for state in states:
#         if state["machine_id"] not in mach_cpu:
#             mach_cpu[state["machine_id"]] = []
#         mach_cpu[state["machine_id"]].append(state['cpu_percent'])

#     prs_cpu = {}

#     for process in processes:
#         if process["machine_id"] not in prs_cpu:
#             prs_cpu[process["machine_id"]] = {}
#         if process['pid'] not in prs_cpu[process["machine_id"]]:
#             prs_cpu[process["machine_id"]][process['pid']] = []
#         prs_cpu[process["machine_id"]][process['pid']].append(
#             process['cpu_percent'])

#     gpu_percent = {}

#     for state in states:
#         if state["machine_id"] not in gpu_percent:
#             gpu_percent[state["machine_id"]] = []
#         gpu_percent[state["machine_id"]].append(state['gpu_memory_percent'])

#     prs_gpu_percent = {}

#     for process in processes:
#         if process["machine_id"] not in prs_gpu_percent:
#             prs_gpu_percent[process["machine_id"]] = {}
#         if process['pid'] not in prs_gpu_percent[process["machine_id"]]:
#             prs_gpu_percent[process["machine_id"]][process['pid']] = []
#         prs_gpu_percent[process["machine_id"]][process['pid']].append(
#             process['gpu_memory_percent'])

#     # only update graph if the machine_id is selected
#     if machine_id in mach_cpu:
#         st.line_chart(mach_cpu[machine_id])
#         # st.write(prs_cpu[machine_id])
#         st.line_chart(gpu_percent[machine_id])
#         # st.write(prs_gpu_percent[machine_id])
#     # update every 5 seconds
#     time.sleep(5)
