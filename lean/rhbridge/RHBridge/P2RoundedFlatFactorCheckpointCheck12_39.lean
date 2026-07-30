import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel12FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel12FlatComponentChunk39

end RHP2Bridge
