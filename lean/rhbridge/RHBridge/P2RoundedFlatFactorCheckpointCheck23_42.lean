import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel23FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel23FlatComponentChunk42

end RHP2Bridge
