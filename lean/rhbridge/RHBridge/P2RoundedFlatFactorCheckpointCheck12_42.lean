import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel12FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel12FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel12FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel12TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel12FlatComponentChunk42

end RHP2Bridge
