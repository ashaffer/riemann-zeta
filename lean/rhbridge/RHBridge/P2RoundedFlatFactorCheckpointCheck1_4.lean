import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel1FlatEven4 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel1FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel1FlatEven4 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel1FlatComponentChunk4

end RHP2Bridge
