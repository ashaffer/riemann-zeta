import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel22FlatEven0 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven0 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel22FlatComponentChunk0

end RHP2Bridge
