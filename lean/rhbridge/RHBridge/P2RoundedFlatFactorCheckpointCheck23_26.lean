import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel23FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel23FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel23FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel23TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel23FlatComponentChunk26

end RHP2Bridge
