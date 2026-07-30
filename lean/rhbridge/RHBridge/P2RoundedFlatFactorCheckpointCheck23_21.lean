import RHBridge.P2RoundedFlatFactorCheckpointData23

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel23FlatEven21 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel23FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel23FlatEven21 =
      (P2RoundedFactorCheckpointData.panel23TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel23FlatComponentChunk21

end RHP2Bridge
