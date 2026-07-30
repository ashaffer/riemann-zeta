import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel2FlatEven10 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven10 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel2FlatComponentChunk10

end RHP2Bridge
