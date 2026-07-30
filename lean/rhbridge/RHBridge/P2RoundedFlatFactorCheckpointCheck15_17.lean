import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel15FlatEven17 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel15FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel15FlatEven17 =
      (P2RoundedFactorCheckpointData.panel15TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel15FlatComponentChunk17

end RHP2Bridge
