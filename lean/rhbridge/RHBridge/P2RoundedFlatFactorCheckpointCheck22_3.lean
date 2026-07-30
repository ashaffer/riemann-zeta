import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel22FlatEven3 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven3 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel22FlatComponentChunk3

end RHP2Bridge
