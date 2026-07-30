import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk11 :
    P2RoundedFactorCheckpointData.panel15FlatEven11 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel15FlatEven11_eq :
    P2RoundedFactorCheckpointData.panel15FlatEven11 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  exact panel15FlatComponentChunk11

end RHP2Bridge
