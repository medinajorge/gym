import pandas as pd

def process_week(w, num):
    W = pd.concat(w.values(), axis=1)
    W.columns = pd.MultiIndex.from_tuples((f"W{num}", day, ex) for day, ex_all in w.items() for ex in ex_all.columns)
    return W

def join_weeks(env):
    i = 1
    weeks = []
    while f"w{i}" in env:
        weeks.append(process_week(env[f"w{i}"], i))
        i += 1
    routine = pd.concat(weeks, axis=1)
    routine.columns.names = ("Week", "Day", "Exercise")
    return routine