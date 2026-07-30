import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel12FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel12FlatComponentChunk29

end RHP2Bridge
