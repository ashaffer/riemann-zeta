import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel12FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel12FlatComponentChunk31

end RHP2Bridge
