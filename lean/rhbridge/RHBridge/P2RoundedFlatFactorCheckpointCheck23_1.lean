import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel23FlatEven1 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel23FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel23FlatEven1 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel23FlatComponentChunk1

end RHP2Bridge
