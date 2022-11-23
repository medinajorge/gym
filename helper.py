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

def deload(R, volume_mpl=2/3, intensity_mpl=0.9, mode="volume"):
    """
    R: routine DataFrame.
    NOTE: if mode == 'volume'  =>  the important thing is the volume. Sets and reps can be adjusted arbitrarily
                                   (and in agreement with the mesocycle).
    """
    R, notes = R.iloc[:-1], R.iloc[-1]    
    week_avg = R.groupby(level=[1,2], axis=1).apply(lambda x: x.mean(axis=1))
    week_deload = week_avg.copy()
    
    if mode == "sets":
        week_deload.loc["sets"] *= volume_mpl
    elif mode == "volume":
        week_deload.loc["volume"] = week_deload.loc["sets"] * week_deload.loc["reps"] * volume_mpl
        week_deload = week_deload.iloc[[0, 1, -1] + [*range(2, week_deload.shape[0] - 1)]]
    else:
        raise ValueError(f"mode '{mode}' not valid. Available: 'sets', 'volume'")
        
    week_deload.loc["weight"] *= intensity_mpl
    week_deload = week_deload.round(1)
    week_deload.loc["notes"] = notes.groupby(level=[1, 2]).apply(lambda x: " || ".join([*x.dropna().unique()]))
    week_deload = week_deload[R.columns.get_level_values(1).unique()] # ordered
    return week_deload