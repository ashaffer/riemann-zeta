import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel22FlatEven14 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven14 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel22FlatComponentChunk14

end RHP2Bridge
