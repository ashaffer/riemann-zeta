import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel22FlatEven17 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven17 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel22FlatComponentChunk17

end RHP2Bridge
