import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel12FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel12FlatComponentChunk25

end RHP2Bridge
