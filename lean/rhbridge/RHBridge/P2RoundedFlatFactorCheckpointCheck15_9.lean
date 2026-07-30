import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk9 :
    P2RoundedFactorCheckpointData.panel15FlatEven9 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel15FlatEven9_eq :
    P2RoundedFactorCheckpointData.panel15FlatEven9 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  exact panel15FlatComponentChunk9

end RHP2Bridge
