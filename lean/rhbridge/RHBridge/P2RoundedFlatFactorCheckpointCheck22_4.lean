import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel22FlatEven4 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven4 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel22FlatComponentChunk4

end RHP2Bridge
