import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel23FlatEven10 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel23FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel23FlatEven10 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel23FlatComponentChunk10

end RHP2Bridge
