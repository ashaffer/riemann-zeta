import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk9 :
    P2RoundedFactorCheckpointData.panel14FlatEven9 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven9_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven9 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  exact panel14FlatComponentChunk9

end RHP2Bridge
