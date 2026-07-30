import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel22FlatEven7 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven7 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel22FlatComponentChunk7

end RHP2Bridge
