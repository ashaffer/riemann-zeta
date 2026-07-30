import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk2 :
    P2RoundedFactorCheckpointData.panel14Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix8_eq :
    P2RoundedFactorCheckpointData.panel14Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk2.1

theorem panel14Prefix9_eq :
    P2RoundedFactorCheckpointData.panel14Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk2.2.1

theorem panel14Prefix10_eq :
    P2RoundedFactorCheckpointData.panel14Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk2.2.2.1

theorem panel14Prefix11_eq :
    P2RoundedFactorCheckpointData.panel14Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk2.2.2.2

end RHP2Bridge
