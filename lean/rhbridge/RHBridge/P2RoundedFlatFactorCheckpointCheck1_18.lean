import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk18 :
    P2RoundedFactorCheckpointData.panel1FlatEven18 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel1FlatEven18_eq :
    P2RoundedFactorCheckpointData.panel1FlatEven18 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨18, by decide⟩ := by
  exact panel1FlatComponentChunk18

end RHP2Bridge
