import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel15FlatEven14 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel15FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel15FlatEven14 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel15FlatComponentChunk14

end RHP2Bridge
