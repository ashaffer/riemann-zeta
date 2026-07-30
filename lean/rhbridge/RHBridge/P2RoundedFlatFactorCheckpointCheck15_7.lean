import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel15FlatEven7 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel15FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel15FlatEven7 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel15FlatComponentChunk7

end RHP2Bridge
