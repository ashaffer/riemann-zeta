import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel12FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel12FlatComponentChunk38

end RHP2Bridge
