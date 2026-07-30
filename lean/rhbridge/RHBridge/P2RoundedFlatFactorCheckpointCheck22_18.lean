import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel22FlatEven18 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven18 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel22FlatComponentChunk18

end RHP2Bridge
