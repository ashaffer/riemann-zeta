import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk9 :
    P2RoundedFactorCheckpointData.panel25FlatEven9 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel25FlatEven9_eq :
    P2RoundedFactorCheckpointData.panel25FlatEven9 =
      (P2RoundedFactorCheckpointData.panel25TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  exact panel25FlatComponentChunk9

end RHP2Bridge
