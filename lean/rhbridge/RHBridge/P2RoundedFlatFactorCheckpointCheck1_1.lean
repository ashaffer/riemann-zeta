import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel1FlatEven1 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel1FlatEven1 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel1FlatComponentChunk1

end RHP2Bridge
