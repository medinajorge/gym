import pandas as pd
from helper import join_weeks

def Eric_cycle1():
    w1 = dict(
        M = pd.concat([
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=3.25, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=6, weight=None, rir=None, distance=3.5, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=2, reps=3, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="St. Dragon Flag iso"),
            pd.Series(dict(sets=2, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=2, reps=None, weight=15, rir=3, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=2, reps=6, weight=60, rir=3, distance=None, notes=None), name="Pause CG BP"),
            pd.Series(dict(sets=2, reps=8, weight=5, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=30, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=1, reps=13, weight=27, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=1, reps=8, weight=10, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=2, reps=5, weight=None, rir=None, distance=3.25, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=5, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="CG Chin Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=1, reps=20, weight=None, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="Seated biceps - offset grip"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="Standing rope ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=None, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=3, reps=10, weight=None, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=2, reps=10, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=2, reps=15, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    w2 = dict(
        M = pd.concat([
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=6, weight=None, rir=None, distance=3.75, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=2, reps=3, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="St. Dragon Flag iso"),
            pd.Series(dict(sets=2, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=16, rir=3, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=3, reps=6, weight=65, rir=3, distance=None, notes=None), name="Pause CG BP"),
            pd.Series(dict(sets=2, reps=8, weight=10, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=35, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=30, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=12.5, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=2, reps=5, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=5, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="CG Chin Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=1, reps=20, weight=4, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=1, reps=12, weight=12.5, rir=0, distance=None, notes=None), name="Seated biceps - offset grip"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="Standing rope ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=115, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=3, reps=10, weight=None, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=2, reps=10, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=2, reps=15, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    
    w3 = dict(
        M = pd.concat([
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=4, reps=12, weight=None, rir=3, distance=None, notes="reps: seconds"), name="Adv Tucked FL"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=4, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=2, reps=3, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="St. Dragon Flag iso"),
            pd.Series(dict(sets=3, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=20, rir=2, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=3, reps=6, weight=67.5, rir=2, distance=None, notes=None), name="Pause CG BP"),
            pd.Series(dict(sets=2, reps=8, weight=12, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=37.5, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=32.5, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=15, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=2, reps=5, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=5, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="CG Chin Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=2, reps=20, weight=4, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=2, reps=12, weight=12.5, rir=0, distance=None, notes=None), name="Seated biceps - offset grip"),    
            pd.Series(dict(sets=2, reps=12, weight=None, rir=0, distance=None, notes=None), name="Standing rope ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=117.5, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=65, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=3, reps=10, weight=65, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=2, reps=10, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=2, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    
    w4 = dict(
        M = pd.concat([
            pd.Series(dict(sets=4, reps=6, weight=None, rir=None, distance=2.75, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=4, reps=12, weight=None, rir=3, distance=None, notes="reps: seconds"), name="Adv Tucked FL"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=4, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=3, reps=3, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=4, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="St. Dragon Flag iso"),
            pd.Series(dict(sets=4, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=4, reps=None, weight=22.5, rir=1, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=4, reps=6, weight=70, rir=1, distance=None, notes=None), name="Pause CG BP"),
            pd.Series(dict(sets=2, reps=8, weight=15, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=40, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=35, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=17.5, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=2, reps=5, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=5, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="CG Chin Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=2, reps=20, weight=4, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=2, reps=12, weight=12.5, rir=0, distance=None, notes=None), name="Seated biceps - offset grip"),    
            pd.Series(dict(sets=2, reps=12, weight=None, rir=0, distance=None, notes=None), name="Standing rope ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=120, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=67.5, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=3, reps=10, weight=67.5, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=3, reps=10, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=3, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    
    w5 = dict(
        M = pd.concat([
            pd.Series(dict(sets=4, reps=6, weight=None, rir=None, distance=2.75, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=4, reps=12, weight=None, rir=3, distance=None, notes="reps: seconds"), name="Adv Tucked FL"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=4, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=3, reps=3, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=4, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="St. Dragon Flag iso"),
            pd.Series(dict(sets=4, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=25, rir=1, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=4, reps=6, weight=70, rir=1, distance=None, notes=None), name="Pause CG BP"),
            pd.Series(dict(sets=3, reps=8, weight=15, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=40, rir=1, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=35, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=17.5, rir=1, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=2, reps=5, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=5, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="CG Chin Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=2, reps=20, weight=4, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=2, reps=12, weight=12.5, rir=0, distance=None, notes=None), name="Seated biceps - offset grip"),    
            pd.Series(dict(sets=2, reps=12, weight=None, rir=0, distance=None, notes=None), name="Standing rope ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=120, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=70, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=3, reps=10, weight=70, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=3, reps=8, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=3, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    
    w6 = dict(
        M = pd.concat([
            pd.Series(dict(sets=4, reps=6, weight=None, rir=None, distance=2.5, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=4, reps=12, weight=None, rir=3, distance=None, notes="reps: seconds"), name="Adv Tucked FL"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=4, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=3, reps=3, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=4, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="St. Dragon Flag iso"),
            pd.Series(dict(sets=4, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=4, reps=None, weight=27.5, rir=1, distance=None, notes="First set: rir 0"), name="W. Pull up (prono)"),
            pd.Series(dict(sets=4, reps=6, weight=72.5, rir=1, distance=None, notes=None), name="Pause CG BP"),
            pd.Series(dict(sets=3, reps=8, weight=17.5, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=3, reps=8, weight=42.5, rir=1, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=35, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=20, rir=1, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=3, reps=5, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Pike PU"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=5, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=3, reps=None, weight=None, rir=2, distance=None, notes=None), name="CG Chin Up"),
            pd.Series(dict(sets=3, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=2, reps=20, weight=4, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=2, reps=12, weight=12.5, rir=0, distance=None, notes=None), name="Seated biceps - offset grip"),    
            pd.Series(dict(sets=2, reps=12, weight=None, rir=0, distance=None, notes=None), name="Standing rope ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=120, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=70, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=3, reps=10, weight=70, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=3, reps=8, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=3, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    return join_weeks(locals())


def Eric_cycle2():
    w1 = dict(
        M = pd.concat([
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=3.25, notes="Distance: #feet"), name="Box Pike PU"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="1-leg FL"),
            pd.Series(dict(sets=2, reps=6, weight=None, rir=None, distance=3.75, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=3, reps=2, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="Full Dragon Flag iso"),
            pd.Series(dict(sets=2, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=2, reps=None, weight=20, rir=3, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=2, reps=6, weight=55, rir=3, distance=None, notes=None), name="Pause CG inclined BP"),
            pd.Series(dict(sets=2, reps=8, weight=20, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=40, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=1, reps=13, weight=35, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=1, reps=8, weight=20, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes="Distance: #feet"), name="HSPU back-to-wall"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Wide Pull Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=1, reps=20, weight=None, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="Barbell drag curl"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="1-arm overhead tricep ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=120, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=2, reps=6, weight=70, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=2, reps=10, weight=70, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=2, reps=8, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=3, reps=None, weight=None, rir=0, distance=None, notes=None), name="Hanging leg raise"),
            pd.Series(dict(sets=3, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    w2 = dict(
        M = pd.concat([
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Box Pike PU"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="1-leg FL"),
            pd.Series(dict(sets=2, reps=6, weight=None, rir=None, distance=4, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=3, reps=2, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="Full Dragon Flag iso"),
            pd.Series(dict(sets=2, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=20, rir=3, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=3, reps=6, weight=55, rir=3, distance=None, notes=None), name="Pause CG inclined BP"),
            pd.Series(dict(sets=2, reps=8, weight=20, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=40, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=37.5, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=22.5, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes="Distance: #feet"), name="HSPU back-to-wall"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Wide Pull Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=1, reps=20, weight=None, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="Barbell drag curl"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="1-arm overhead tricep ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=2, reps=8, weight=120, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=2, reps=6, weight=70, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=2, reps=10, weight=70, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=2, reps=8, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=3, reps=None, weight=None, rir=0, distance=None, notes=None), name="Hanging leg raise"),
            pd.Series(dict(sets=3, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    
    w3 = dict(
        M = pd.concat([
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Box Pike PU"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="1-leg FL"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=4, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=3, reps=2, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="Full Dragon Flag iso"),
            pd.Series(dict(sets=2, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=20, rir=3, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=3, reps=6, weight=50, rir=3, distance=None, notes=None), name="Pause CG inclined BP"),
            pd.Series(dict(sets=2, reps=8, weight=20, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=2, reps=8, weight=40, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=37.5, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=25, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=None, rir=2, distance=None, notes="Distance: #feet"), name="HSPU back-to-wall"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Wide Pull Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=1, reps=20, weight=None, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="Barbell drag curl"),    
            pd.Series(dict(sets=1, reps=12, weight=None, rir=0, distance=None, notes=None), name="1-arm overhead tricep ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=3, reps=8, weight=120, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=70, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=2, reps=10, weight=70, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=2, reps=8, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=3, reps=None, weight=None, rir=0, distance=None, notes=None), name="Hanging leg raise"),
            pd.Series(dict(sets=3, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    
    w4 = dict(
        M = pd.concat([
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=3, notes="Distance: #feet"), name="Box Pike PU"),
            pd.Series(dict(sets=4, reps=1, weight=None, rir=3, distance=None, notes=None), name="1-leg FL"),
            pd.Series(dict(sets=3, reps=6, weight=None, rir=None, distance=4.25, notes="Distance: #hand"), name="Lean PU"),
            pd.Series(dict(sets=3, reps=2, weight=2, rir=None, distance=None, notes="4 seconds. 1 sec pause in middle. weight: yellow band"), name="St. HW ecc FL - band"),
            pd.Series(dict(sets=2, reps=1, weight=None, rir=0, distance=None, notes="max hold"), name="Full Dragon Flag iso"),
            pd.Series(dict(sets=2, reps=None, weight=2, rir=0, distance=None, notes="yellow band"), name="Facepulls")
        ], axis=1),
    
        X = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=22.5, rir=3, distance=None, notes=None), name="W. Pull up (prono)"),
            pd.Series(dict(sets=3, reps=6, weight=52.5, rir=3, distance=None, notes=None), name="Pause CG inclined BP"),
            pd.Series(dict(sets=3, reps=8, weight=20, rir=None, distance=None, notes=None), name="W. ring row"),
            pd.Series(dict(sets=3, reps=8, weight=42.5, rir=2, distance=None, notes=None), name="Militar"),
            pd.Series(dict(sets=2, reps=13, weight=40, rir=1, distance=None, notes=None), name="1-arm cable row"),
            pd.Series(dict(sets=2, reps=8, weight=27.5, rir=2, distance=None, notes=None), name="W. dip")
        ], axis=1),
        
        V = pd.concat([
            pd.Series(dict(sets=3, reps=None, weight=None, rir=1, distance=None, notes="Distance: #feet"), name="HSPU back-to-wall"),
            pd.Series(dict(sets=3, reps=1, weight=None, rir=3, distance=None, notes=None), name="Adv Tucked FL"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Wide Pull Up"),
            pd.Series(dict(sets=2, reps=None, weight=None, rir=2, distance=None, notes=None), name="Ring PU"),
            pd.Series(dict(sets=2, reps=20, weight=None, rir=0, distance=None, notes=None), name="Chest-supported delt raise"),    
            pd.Series(dict(sets=2, reps=12, weight=None, rir=0, distance=None, notes=None), name="Barbell drag curl"),    
            pd.Series(dict(sets=2, reps=12, weight=None, rir=0, distance=None, notes=None), name="1-arm overhead tricep ext")
        ], axis=1),
    
        S = pd.concat([
            pd.Series(dict(sets=3, reps=8, weight=120, rir=2, distance=None, notes=None), name="Hip Thrust"),
            pd.Series(dict(sets=3, reps=6, weight=70, rir=2, distance=None, notes=None), name="Squat"),
            pd.Series(dict(sets=2, reps=10, weight=70, rir=3, distance=None, notes="Straps"), name="Romanian DL"),
            pd.Series(dict(sets=2, reps=8, weight=None, rir=2, distance=None, notes="Straps"), name="Split squat"),
            pd.Series(dict(sets=3, reps=None, weight=None, rir=0, distance=None, notes=None), name="Hanging leg raise"),
            pd.Series(dict(sets=3, reps=12, weight=15, rir=None, distance=None, notes=None), name="GHD back ext")
        ], axis=1)
    )
    return join_weeks(locals())