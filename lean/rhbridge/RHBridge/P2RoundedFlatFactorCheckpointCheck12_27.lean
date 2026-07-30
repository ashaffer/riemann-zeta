import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel12FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel12FlatComponentChunk27

end RHP2Bridge
