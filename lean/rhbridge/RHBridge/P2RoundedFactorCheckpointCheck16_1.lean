import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk1 :
    P2RoundedFactorCheckpointData.panel16Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix4_eq :
    P2RoundedFactorCheckpointData.panel16Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk1.1

theorem panel16Prefix5_eq :
    P2RoundedFactorCheckpointData.panel16Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk1.2.1

theorem panel16Prefix6_eq :
    P2RoundedFactorCheckpointData.panel16Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk1.2.2.1

theorem panel16Prefix7_eq :
    P2RoundedFactorCheckpointData.panel16Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk1.2.2.2

end RHP2Bridge
