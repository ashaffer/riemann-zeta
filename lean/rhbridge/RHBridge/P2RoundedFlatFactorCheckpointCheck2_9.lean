import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk9 :
    P2RoundedFactorCheckpointData.panel2FlatEven9 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven9_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven9 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  exact panel2FlatComponentChunk9

end RHP2Bridge
