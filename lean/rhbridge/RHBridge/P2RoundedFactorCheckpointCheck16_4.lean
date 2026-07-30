import RHBridge.P2RoundedFactorCheckpointData16

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16FactorChunk4 :
    P2RoundedFactorCheckpointData.panel16Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨16, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel16Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨16, by decide⟩ := by
  decide +kernel

theorem panel16Prefix16_eq :
    P2RoundedFactorCheckpointData.panel16Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk4.1

theorem panel16Prefix17_eq :
    P2RoundedFactorCheckpointData.panel16Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk4.2.1

theorem panel16Prefix18_eq :
    P2RoundedFactorCheckpointData.panel16Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk4.2.2.1

theorem panel16Prefix19_eq :
    P2RoundedFactorCheckpointData.panel16Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨16, by decide⟩ := by
  exact panel16FactorChunk4.2.2.2

end RHP2Bridge
