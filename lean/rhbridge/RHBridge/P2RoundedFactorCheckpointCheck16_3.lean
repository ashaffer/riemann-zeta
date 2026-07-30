import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk3 :
    P2RoundedFactorCheckpointData.panel16Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix12_eq :
    P2RoundedFactorCheckpointData.panel16Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk3.1

theorem panel16Prefix13_eq :
    P2RoundedFactorCheckpointData.panel16Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk3.2.1

theorem panel16Prefix14_eq :
    P2RoundedFactorCheckpointData.panel16Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk3.2.2.1

theorem panel16Prefix15_eq :
    P2RoundedFactorCheckpointData.panel16Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk3.2.2.2

end RHP2Bridge
