import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel23FlatEven2 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel23FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel23FlatEven2 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel23FlatComponentChunk2

end RHP2Bridge
