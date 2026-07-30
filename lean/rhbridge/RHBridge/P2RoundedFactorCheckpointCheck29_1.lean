import RHBridge.P2RoundedFactorCheckpointData29

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29FactorChunk1 :
    P2RoundedFactorCheckpointData.panel29Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨29, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel29Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨29, by decide⟩ := by
  decide +kernel

theorem panel29Prefix4_eq :
    P2RoundedFactorCheckpointData.panel29Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk1.1

theorem panel29Prefix5_eq :
    P2RoundedFactorCheckpointData.panel29Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk1.2.1

theorem panel29Prefix6_eq :
    P2RoundedFactorCheckpointData.panel29Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk1.2.2.1

theorem panel29Prefix7_eq :
    P2RoundedFactorCheckpointData.panel29Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨29, by decide⟩ := by
  exact panel29FactorChunk1.2.2.2

end RHP2Bridge
