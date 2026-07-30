import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel23FlatEven15 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel23FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel23FlatEven15 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel23FlatComponentChunk15

end RHP2Bridge
