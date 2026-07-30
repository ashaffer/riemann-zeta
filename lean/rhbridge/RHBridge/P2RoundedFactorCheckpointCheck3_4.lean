import RHBridge.P2RoundedFactorCheckpointData3

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3FactorChunk4 :
    P2RoundedFactorCheckpointData.panel3Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨3, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel3Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨3, by decide⟩ := by
  decide +kernel

theorem panel3Prefix16_eq :
    P2RoundedFactorCheckpointData.panel3Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk4.1

theorem panel3Prefix17_eq :
    P2RoundedFactorCheckpointData.panel3Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk4.2.1

theorem panel3Prefix18_eq :
    P2RoundedFactorCheckpointData.panel3Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk4.2.2.1

theorem panel3Prefix19_eq :
    P2RoundedFactorCheckpointData.panel3Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨3, by decide⟩ := by
  exact panel3FactorChunk4.2.2.2

end RHP2Bridge
