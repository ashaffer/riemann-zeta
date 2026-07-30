import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel2FlatEven4 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven4 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel2FlatComponentChunk4

end RHP2Bridge
