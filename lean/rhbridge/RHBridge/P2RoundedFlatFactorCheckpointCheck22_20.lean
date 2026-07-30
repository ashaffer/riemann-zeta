import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk20 :
    P2RoundedFactorCheckpointData.panel22FlatEven20 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven20_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven20 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨20, by decide⟩ := by
  exact panel22FlatComponentChunk20

end RHP2Bridge
