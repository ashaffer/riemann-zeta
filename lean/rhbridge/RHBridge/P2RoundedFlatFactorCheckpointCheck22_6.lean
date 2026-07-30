import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel22FlatEven6 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven6 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel22FlatComponentChunk6

end RHP2Bridge
