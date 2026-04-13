# Reflection: Profile Pair Comparisons

## Pair 1: Pop/Sad/High-Energy/Acoustic vs Classical/Intense/Low-Energy/Non-Acoustic
The pop/sad/high-energy profile surfaced fast, intense tracks (for example `Gym Hero`) because the high target energy dominated when `sad` had no catalog match. The classical/intense/low-energy profile shifted toward calmer songs (`Lantern Waltz`, `Spacewalk Thoughts`) because the low target energy strongly rewarded low-intensity tracks. This difference makes sense because the energy target moved from an extreme high value to an extreme low value.

## Pair 2: Pop/Sad/High-Energy/Acoustic vs Unseen-Genre/Focused/Max-Energy
Both profiles ended up recommending high-energy songs, but for different reasons: the pop profile still got some genre benefit from `pop` matches, while the unseen-genre profile could not use genre at all and relied mostly on energy plus low-acoustic bonuses. This makes sense because removing a valid genre anchor forces the model to lean on continuous features.

## Pair 3: Classical/Intense/Low-Energy/Non-Acoustic vs Unseen-Genre/Focused/Max-Energy
The classical/low-energy profile favored mellow tracks and included a classical match at the top, while the unseen-genre/max-energy profile favored very intense tracks across many genres. The outputs diverged sharply because the target energy moved from near-minimum to maximum and one profile had at least one valid genre anchor (`classical`) while the other had none (`drill`). This validates that the recommender is primarily testing intensity fit first when category signals are weak.
