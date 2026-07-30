import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk26 :
    P2RoundedFactorCheckpointData.panel1FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd2_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd2 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨2, by decide⟩ := by
  exact panel1FlatComponentChunk26

end RHP2Bridge
