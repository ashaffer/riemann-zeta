import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel2FlatEven22 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven22 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel2FlatComponentChunk22

end RHP2Bridge
