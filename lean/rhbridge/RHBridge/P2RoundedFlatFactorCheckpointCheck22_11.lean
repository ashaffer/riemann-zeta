import RHBridge.P2RoundedFlatFactorCheckpointData22

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22FlatComponentChunk11 :
    P2RoundedFactorCheckpointData.panel22FlatEven11 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel22FlatEven11_eq :
    P2RoundedFactorCheckpointData.panel22FlatEven11 =
      (P2RoundedFactorCheckpointData.panel22TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  exact panel22FlatComponentChunk11

end RHP2Bridge
