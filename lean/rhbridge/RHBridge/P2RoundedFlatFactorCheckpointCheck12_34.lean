import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel12FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel12FlatComponentChunk34

end RHP2Bridge
